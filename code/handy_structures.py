import pandas as pd
from collections import Counter
from tqdm import *
import operator

def get_mids_per_sender(dataset_set):
    '''
    Computes a dictionnary which contains, for each sender in the dataset_set, the list of ones mails. 
    INPUT
    dataset_set : even training_set or test_set
    OUTPUT
    emails_ids_per_sender : a dictionnary containing all emails ids per sender
    '''
	
    #create a new dictionnary	
    emails_ids_per_sender = {} 
	
    #iterate on each sender
    for index, series in dataset_set.iterrows(): #series contains senders and mids
        row = series.tolist() #we get a list of with the sender at position 0 and each of ones mails
        sender = row[0] #this is the sender
        ids = row[1:][0].split(' ') #we get a list with all the mids
        emails_ids_per_sender[sender] = ids #we add them in the dictionnary
        # In the dataset_set, one sender is different from the others	
		
    return emails_ids_per_sender
	
def get_address_books(dataset_info, dataset_set):
    '''
    Computes address book with frequency information for each user
    '''
    
    address_books = {} #a new dictionnary
    i = 0
	
    emails_ids_per_sender = get_mids_per_sender(dataset_set)

    for sender, ids in tqdm(emails_ids_per_sender.items()): #for key and value of the dictionnary
        recs_temp = [] #will contain the recipients
        for my_id in ids: #for each mail
            recipients = dataset_info[dataset_info['mid'] == my_id]['recipients'].tolist() #list of all the recipients
            recipients = recipients[0].split(' ') #get a list of all the recipients
            # keep only legitimate email addresses (*)
            recipients = [rec for rec in recipients if '@' in rec]
            recs_temp.append(recipients)
        # flatten    
        recs_temp = [elt for sublist in recs_temp for elt in sublist] #one list
        # compute recipient counts
        rec_occ = dict(Counter(recs_temp)) #we count the times the sender sent a mail to someone
        # order by frequency
        sorted_rec_occ = sorted(rec_occ.items(), key=operator.itemgetter(1), reverse = True)
        # save
        address_books[sender] = sorted_rec_occ
        
    return address_books
	
def transform_dataset(dataset_info, dataset_set):	
    '''
    Create a dataframe with all info for both training and test, sorted by date
        number of rows  = #mails
        columns : mid + date + body + sender + (recipients)
    '''

    #create a dataframe which contains the senders of each mail
    senders_df = pd.DataFrame()   

    #Get all mails sent by everybody
    emails_ids_per_sender = get_mids_per_sender(dataset_set)

    # Transformation of datasets
    for sender, ids in tqdm(emails_ids_per_sender.items()): #for key and value of the dictionnary
        for my_id in ids: #for each mail
            senders_df = senders_df.append({'mid':my_id, 'sender':sender}, ignore_index = True)

    dataset_df = senders_df.merge(dataset_info, how='left', on='mid')	

    #Need to transform recipients with splits
    #if 'recipients' in dataset_df.columns:
    #    for row in range(dataset_df.shape[0]):
    #        dataset_df['recipients'][row] = dataset_df['recipients'][row].split(' ')

    #Sort by the date 
    dataset_df = dataset_df.sort_values('date')
    
    #Clean the index
    dataset_df = dataset_df.reset_index(drop=True)
            
    return dataset_df