from instaloader import Instaloader, Profile
import os
import pandas as pd

# Create object
insta = Instaloader(dirname_pattern='static/data/{target}/posts/uploaded')
# Target will be username perhaps if you want to save posts just enable by save=True
def insta_posts(TARGET:str,save:bool=False):
    # Create the post info list in order to store it.
    post_info=[]
    if not TARGET:
        TARGET = "shakira"

    # Set Username
    profile = Profile.from_username(
        insta.context,
        TARGET
    )

    # Get Posts
    uploaded_posts = profile.get_posts()

    # custom save folder
    save_folder = os.path.join(
        "static",
        "data",
        TARGET,
        "posts",
        "uploaded"
    )
    if not(os.path.isdir(save_folder)):
        os.makedirs(save_folder)
    # Start Saving posts with a count

    for post in uploaded_posts:
        
        try:
            title=post.title
            caption=post.caption
            date=post.date
            url=post.url
            
            post_info.append([TARGET,title,caption,date,url])
            if save:
                insta.download_post(
                    post,
                    target=TARGET
                )    

            
        except:
            continue
    
    df=pd.DataFrame(post_info,columns=['profile_name','post_title','caption','date','url'])
    df.to_csv(f'{TARGET}.csv',index=False)

    return post_info

  

#insta_posts(TARGET='future')
    