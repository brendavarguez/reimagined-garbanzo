## Challenges
There are two different python scripts to answer the questions from each challenge. You can either run the two scripts separetely from terminal, or you can just run the bash script which automatically does the set up and runs both scripts itself. You can run the the bash script in the following way:

```
bash full_script.sh
```

> Note: Please first check the script bash before executing due to there is a set up with docker that you might or might not need.

<br>  

### Python Challenge (manual execution)
 - Install the right libraries from the **requirements** file: `pip install -r requirements.txt`
 - Running challenge script: `python python_challenge.py`

<br>  

#### Challenge 1 answers:
1. Get number of answered and unanswered questions
    - Answered questions: 21
    - Unanswered questions: 9
    
<br>  

2. Answer with least views:

    This is the answer with least views having 8 views in total.
    ```
    {'answer_count': 0,
     'content_license': 'CC BY-SA 4.0',
     'creation_date': 1659057371,
     'is_answered': False,
     'last_activity_date': 1659057371,
     'link': 'https://stackoverflow.com/questions/73160676/is-there-an-automatic-way-to-build-the-changes-file-from-git-log-when-publis',
     'owner': {'display_name': 'KJ7LNW',
               'link': 'https://stackoverflow.com/users/14055985/kj7lnw',
               'profile_image': 'https://i.stack.imgur.com/A6il4.png?s=256&g=1',
               'reputation': 899,
               'user_id': 14055985,
               'user_type': 'registered'},
     'question_id': 73160676,
     'score': 0,
     'tags': ['perl', 'module', 'release', 'cpan'],
     'title': 'Is there an automatic way to build the &quot;Changes&quot; file '
              'from `git log` when publishing a perl module?',
     'view_count': 8}
    ```
<br>  

3. Get oldest and newest answers:

    Oldest answer published on 2010-03-21 10:43:23:

    ```
    {'answer_count': 5,
    'content_license': 'CC BY-SA 2.5',
    'creation_date': datetime.datetime(2010, 3, 21, 10, 43, 23),
    'is_answered': True,
    'last_activity_date': 1659052453,
    'last_edit_date': 1269193107,
    'link': 'https://stackoverflow.com/questions/2487829/whats-the-right-way-to-kill-child-processes-in-perl-before-exiting',
    'owner': {'accept_rate': 62,
              'display_name': 'rarbox',
              'link': 'https://stackoverflow.com/users/296645/rarbox',
              'profile_image': 'https://www.gravatar.com/avatar/0fcc3a65dc2842d7473aba9448e53fc0?s=256&d=identicon&r=PG',
              'reputation': 486,
              'user_id': 296645,
              'user_type': 'registered'},
    'question_id': 2487829,
    'score': 6,
    'tags': ['perl', 'fork', 'irc', 'poe'],
    'title': 'What&#39;s the right way to kill child processes in perl before '
             'exiting?',
    'view_count': 9364}
    ```
    <br>  

    Newest answer published on 2022-07-28 20:38:49:

    ```
    {'accepted_answer_id': 73160973,
    'answer_count': 1,
    'content_license': 'CC BY-SA 4.0',
    'creation_date': datetime.datetime(2022, 7, 28, 20, 38, 49),
    'is_answered': True,
    'last_activity_date': 1659060761,
    'last_edit_date': 1659060130,
    'link': 'https://stackoverflow.com/questions/73160771/how-do-you-compare-strings-in-perl',
    'owner': {'display_name': 'Manny',
              'link': 'https://stackoverflow.com/users/12276451/manny',
              'profile_image': 'https://www.gravatar.com/avatar/33f20e204e84e8d915250af1e02cea08?s=256&d=identicon&r=PG&f=1',
              'reputation': 23,
              'user_id': 12276451,
              'user_type': 'registered'},
    'question_id': 73160771,
    'score': 0,
    'tags': ['string', 'algorithm', 'perl'],
    'title': 'How Do You Compare Strings in Perl?',
    'view_count': 21}
    ```
<br>  

4. Get answer from owner with highest reputation
    ```
    {'accepted_answer_id': 3107596,
    'answer_count': 1,
    'content_license': 'CC BY-SA 2.5',
    'creation_date': datetime.datetime(2010, 6, 24, 0, 59, 50),
    'is_answered': True,
    'last_activity_date': 1658925135,
    'link': 'https://stackoverflow.com/questions/3107540/c-public-key-verify-perl-private-key-and-use-as-aes-key-possible-and-or-viabl',
    'owner': {'accept_rate': 100,
              'display_name': 'Prix',
              'link': 'https://stackoverflow.com/users/342740/prix',
              'profile_image': 'https://i.stack.imgur.com/lHbcW.gif?s=256&g=1',
              'reputation': 19233,
              'user_id': 342740,
              'user_type': 'registered'},
    'question_id': 3107540,
    'score': 1,
    'tags': ['c#', 'perl', 'encryption', 'rsa', 'rijndael'],
    'title': 'C# Public Key verify Perl Private key and use as AES key ? Possible '
             'and/or viable?',
    'view_count': 402}
    ```

<br>  

### SQL Challenge (manual execution)
For this challenge it is required python3.8, as well as an environment with access to a PostgreSQL database. You can perform the following steps to do the set up manually:

- Installing docker: `sudo apt install docker-compose`
- Deploy environment: `sudo docker-compose up -d`
- Running challenge script: `python postgres_challenge.py`

<br>  

#### Challenge 2 answers:
1. What is the busiest airport during the year?
    
    Benito Juarez with 3 and La paz with 3

<br>  

2. What is the airline with the highest number of flights during the year?
    
    Aeromar with 3, Interjet with 3

<br>  

3. Which day had the highest number of flights?

    2021-05-02 with 6

<br>  

4. Which airlines have more than 2 flights per day?

    There are no airlines with more than two flights per day
