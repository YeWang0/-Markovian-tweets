# Query a timeline of a certain user
import json
import codecs
import os
from result_handler import *
from TwitterSearch import *

def get_user_timeline_by_name(user_name):
    try:
        #use screen name(str) or user id(int)
        # user_name='Ye__Wang'
        # user_name='BarackObama'
        # user_name='HillaryClinton'
        # user_name='realDonaldTrump'
        tuo = TwitterUserOrder(user_name)
        tuo.set_include_rts(True)
        tuo.set_count(100)#return 100 results per page
        tuo.set_contributor_details(True)
        # it's about time to create TwitterSearch object again
        ts = TwitterSearch(
            consumer_key="cxRBdyw5uF8nX0tUAOd7bkPCu",
            consumer_secret="Kowz2iCaC4yeF84L5jX0ql5m7SMrssPqh3QxyzEz1jLzPSiHqH",

            access_token="724966264419024897-mJeva42j3HAozgjwj2ZMdrSRM7S95kT",
            access_token_secret="o265mwSzlwNE4ZZEYRUMw9xRz5qoIAagCNJKf83l72VOw"
         )

        # start asking Twitter about the timeline
        result=[]
        count=0
        text=''
        for tweet in ts.search_tweets_iterable(tuo):
            # print( '%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            # text=url_remove(tweet['text'])
            text=tweet_cleanup(tweet['text'])
            result.append(text+'\n')
            count+=1
        # print count

        if user_name:
            with codecs.open(os.path.join(os.path.normpath('../result'), 'Timeline_'+user_name+'.txt'), 'w', 'utf-8') as f:
                # json.dump(result, f, indent=4)
                f.writelines(result)
    except TwitterSearchException as e: # catch all those ugly errors
        print(e)

def get_user_timeline_by_id(user_id):
    try:
        #use screen name(str) or user id(int)
        user_id=430228469
        tuo = TwitterUserOrder(user_id)
        tuo.set_include_rts(True)
        tuo.set_count(100)#return 100 results per page
        tuo.set_contributor_details(True)
        # it's about time to create TwitterSearch object again
        ts = TwitterSearch(
            consumer_key="cxRBdyw5uF8nX0tUAOd7bkPCu",
            consumer_secret="Kowz2iCaC4yeF84L5jX0ql5m7SMrssPqh3QxyzEz1jLzPSiHqH",

            access_token="724966264419024897-mJeva42j3HAozgjwj2ZMdrSRM7S95kT",
            access_token_secret="o265mwSzlwNE4ZZEYRUMw9xRz5qoIAagCNJKf83l72VOw"
         )

        # start asking Twitter about the timeline
        result=[]
        count=0
        text=''
        for tweet in ts.search_tweets_iterable(tuo):
            print( '%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
            # text=url_remove(tweet['text'])
            text=tweet_cleanup(tweet['text'])
            result.append(text+'\n')
            count+=1
        print count
        if user_id:
            with codecs.open(os.path.join('result', 'Timeline_'+str(user_id)+'.txt'), 'w', 'utf-8') as f:
                # json.dump(result, f, indent=4)
                f.writelines(result)

    except TwitterSearchException as e: # catch all those ugly errors
        print(e)
