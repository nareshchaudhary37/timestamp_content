# user-friendly-date-maker

The User friendly date maker project represents between passed date and current date time distance with appropricate message.

* How to install

    ```
        git clone https://github.com/nareshchaudhary37/user-friendly-date-maker
        cd user-friendly-date-maker
        python setup.py
    ```

* How to use?

    Do not need to import datetime, timedelta.
    if you already have a date object of created datetime. it's for testing purpose

    ##### 1. If your message sent recently. ###
        
        
        #!python

        from datetime import datetime
        from date_maker import date_maker
        
        created_at = datetime.now() # your message date here
        res = date_maker(created_at)
        print (res.repr)
        
        Output:
        
        Just Now.
        

    ##### 2. if your message sent 2 days ago. ###
        

        
        #!python


        from date_maker import date_maker
        from datetime import datetime, timedelta
        
        created_at = datetime.now() + timedelta(days=2) # your message date here
        res = date_maker(created_at)
        print (res.repr)
        

        Output:
        
        2 Day(s) Ago.
        


:)

