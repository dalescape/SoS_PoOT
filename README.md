# SoS_PoOT
Story of Seasons, Pioneers of Olive Town - Crop Planting Planner
--------------------------------------------------------------------------

# App Planning

I want to be able to go into a simple interface and type in details about where I am currently at in my game including the season, day of season, & be given suggustions on how to best buy seeds and plant crops. This is becuase some crops are only sold in certain seasons, can grow multiple times a season, and other types of things. Considering the amount of time left in a season, profit and seed availability I want to be told what seeds i should buy and what to plant. I also want to see how much I can make from each crop depending on if i produce the seeds or the star level. 

I have a spreadsheet with crop info that i can build on.  

Pages:
- HomePage (UserLoginPage,CreateUserPage)
- UserLoginPage (HomePage,MyFarmPage)
- CreateUserPage (HomePage,MyFarmPage)
- MyFarmPage (HomePage,CropPlannerPage,FarmDetailsPage)
- CropPlannerPage (MyFarmPage)
- FarmDetailsPage (MyFarmPage)

Components:
Navbar


--------------------------------------------------------------------------
# Back at it notes:

Okay so I want to get back into programming. 

I have an idea, making a lil calculator thingy for story of seasons pioneers of olive town to determine what i should plant. Maybe I could add on by user inputting their seeds or whatever and maybe inventory. Goal is just the seed planner first. 

I am stuck figuring out what to do to start since its been a while. 

I remember needing to start with github. Problem i remember is that i need to make sure i have all the stuff on my computer up to date. 

I need to change my file system, too many things on my desktop. 

I can organize my thoughts and previous notes with chat.
———————————————————————————
## 10.9 

Alrighty, going through install fest. Updating my mac, scared to update it to the most recent thingy 15.01 so idk there. updated vscode. updated the terminal oh my zsh.
Open VSCode and open the Command Palette by pressing (Cmd + Shift + P)
Okay now i need to check 
code … works to open vs code
code myfile.txt … opens a specific file
code . … opens the current folder
now check on brew, seems ok after upgrading
checking python, seems a bit off with location in file system. installed python again to get the up to date. but location still off…
now checking pip, it seems okay.
now checking python virtual environment. all good and opened a v.e. called default in the new window terminal. 
cmd + N to get a new window
remember - i need to activate the v.e. every time i want it after the terminal closes.
check node, all good. npm needed updated. npm install -g npm@10.9.0 		
now install latest version of node, now testing 
node worked, got these commands and closed out. npm seems fine too. .break    Sometimes you get stuck, this gets you out
.clear    Alias for .break
.editor   Enter editor mode
.exit     Exit the REPL
.help     Print this help message
.load     Load JS from a file into the REPL session
.save     Save all evaluated commands in this REPL session to a file

Press Ctrl+C to abort current expression, Ctrl+D to exit the REPL

now checking git.
user.name is dalescape and 
 is the email. 
 two code editors = code
github personal token, 30 days


now im all logged in.
checked on aliases. i have the option of setting a default python venv everytime i open the terminal. i think i will hold off for right now. maybe i should get a list of venv’s.We are also going to add another line to our .zshrc to make sure we are using our default Python venv everytime we open the terminal. So below your aliases within .zshrc add:
#/ activate default python venv
source $HOME/default/bin/activate

now i will do postgresql, its updated. got in and exited.

## 10.10 + 11
I have the recommended extensions but might need to update these later. 
Reading over version tracking with Git. Created a repo in Github called SoS_PoOT
Checked my ~ files. I see default, Public, Programming, Postman and sql-workshop as ones I have likely added. Not planning on messing with them today but I do want to try and keep all my stuff under Programming if possible. 

## 10.12
Continuing to go through the curriculum. I see JS, Python and testing ish are next but I think I want to go back to that after I have everything set up. Next I see OOP stuff which I should go back to at a later time. I went to the full stack chapter and it seems they have changed the backend to be Flask, I remember touching this. Nope final project is using Django. 
Okay so I went to an old project that I set up previously not long after graduating. I think I want to clone what I have in there and alter it to what I want to do now. But went back to the old slack and found the personal project info from Aug 7th. It states the following:
Personal Project:

Sites: Trello.com -> create board
Tldraw.com
DrawSql

1. Have a clear objective
2. User stories -> from the perspective of the user, what will they see
3. Draw out each screen -> plan components
4. Design DB schema (drawSql)
5. Back-end (Django)
6. Front-end (React)
7. Deployment (optional)

Francisco Avila (Instructor)
  1:37 PM
@uniform_students I’m noticing a pattern in pull requests that we all may want to watch out for:
* 		Do not push your virtual environment onto github
* 		Please utilize the following link to determine which files should be included in your gitignore https://github.com/github/gitignore/blob/main/Python.gitignore
* 		Hide your secret key in a .env file

Great job everyone keep up the good work

Python.gitignore

I should go to the video on youtube covering fullstack from the aug 7th 2023 start day. found a couple other resources that might be good too. Found the walkthrough, it uses a task manager repo, i think i should do that instead. 
- in terminal i am going to cd to programming and clone my project from github, the SoS_PoOT
- now i need to open this in VS code 
- am in vs code now after coping my notes into the readme 
- in terminal i will cd into this folder, i did and it now has git (main) next to file name. 
- not sure on next step.. do i need to create a venv first ? well i think i should work on the planning steps. I see i need to follow the steps for the backend first and then move onto the front end. i can work with that. i think maybe i should focus on following the steps since i need to refresh on all of that first and then i can continue building. 
- started working on the actual planning. added headers to my readme here. began describing what i want this thing to do. 
- started a sketch in tldraw for pages and stuff. 
- OOOOHHHH i just saw that my last project i was working on was only started with django! i was playing with the data in there and didn't have a front end set up yet so i should be able to focus on the backend i like to wanted first. 
- okay i have the django curriculum pulled up to start working. 
- created new venv called .venv & it added a file in my SoS_PoOT folder. i need to remeber to not add this when i push to git. now i activated it. 
- now i am installing django and was prompted to upgrade. now i will create a django project within my main folder but within a parent directory. this worked and i named it SoS_PoOT_proj 
* please note that i pretty much always need to run the following command for starting a project, its caused issues when i havent, django-admin startproject pokedex_proj #<=== Notice this command is missing a period
- running django admin now, saw list of commands i could run. i need to finish installing stuff (pip install "psycopg[binary]", pip install djangorestframework,pip install django-cors-headers)
- now creating the requirments file (pip freeze > requirements.txt)
- now i will need to create a db in psql, i will call it SoS_PoOT_db 
- the settings need updated for database engine and name and i also added three things under installed apps. 
- next step is to create an app

## 10.13

- not sure what apps to create. probably a user_app which holds the user's farm details on it? and the crop_app, before creating these i want to push this to github. 
- doing git status, added changes and new files to a commit locally. did not include my venv. now pushing to github.. didn't work. now trying (git push -u origin main)
- ran into error due to having my secret token for my github login in here, whoops lol. i will take it out, git add readme.md and then (git commit -- amend --no-edit)-doesn't work! in order to edit the previous commit and not have to create a new one. another idea suggusted by chat is creating a git ignore file.. i think a lot of this stuff will need to be moved to that kind of file. creating one now. now i should add files to it that i want git to skip, for now i just want .venv and .DS_Store not included. going into gitignore file and adding those. now i need to run git status. oooh i think it worked, now the only untracked file is the gitignore one. 
- now to try pushing again. hm didn't work. i think the secret key is still in the old commit. okay i am going back and trying to undo the last commits that still have the secret key. trying git log first. what i got is below

commit 5c2e1817c96f18af44a0f4a18e25328ad02d1f43
 (HEAD -> main)
Author: dalescape <kdalelewis@yahoo.com>
Date:   Sun Oct 13 17:20:04 2024 -0400

    added an ignore file

commit 65a34f5a482d8de1a0251e424521229fd36efa13
Author: dalescape <kdalelewis@yahoo.com>
Date:   Sun Oct 13 16:35:56 2024 -0400

    first commit. working in readme and have started with django project. did not include my venv

commit d68e467d203c5c2e07cdd20436acfa4183816743 (origin/main, origin/HEAD)
Author: dalescape <56903611+dalescape@users.noreply.github.com>
Date:   Fri Oct 11 14:03:23 2024 -0400

eply.github.com>
Date:   Fri Oct 11 14:03:23 2024 -0400

    Initial commit
(END)

- okie so with git reset i will return to the current branch to a specified point. the info i refrered to is below:

The git reset command will return the current branch to a specified previous commit. By default, this command will remove commits from the current branch’s history while leaving the files in the working tree untouched. This allows you to redo one or more commits without losing any work.

When calling git reset, you need to specify the commit to reset to. You can get the hash of the commit you want from git log, or you can specify an ancestor of HEAD, the current commit, using the tilde (~) suffix. 

To undo the last two commits, use the commands:

git add .
git commit -m "This commit is a mistake"
#/ make changes
git add .
git commit -m "This commit is another mistake"
git reset HEAD~2
git add .
git commit -m "this commit corrects both mistakes"

- now i will undo the last two commits. i did "git reset HEAD~2" now running git status. perfect now i will git add all of it. then do git commit with my comment and try pushing it. 

- yayyyy it has worked and i have no problems currently. now back to django. i have two apps to start. i will begin with user_app. i went through old files and found an example project going through the full stack exercise, this will be amazing to refrence. i see the venv is only in the backend. i should probably do that as well envenntually. starting with just the user_app. going into proj. now will create 3 apps. (user_app , crop_app , farm_app) done.
* i should get the terminal history into a file for refrence
- now i need to add these to settings. great now i see something about adding rest_framework into the settings. not sure about this quite yet. eh found it in an old project so going to put in now. 
- next step seems to be define models. but i see an error and i think i should install requirments first. hm says already done. okay now defining models in user_app. stuck on error. tried install all the django stuff again, didn't work. tried reloading window from command palette, didn't work. tried adding "AUTH_USER_MODEL = 'user_app.User'" to settings. Didn't work. okay i had to mess with the python interpreter, it wasn't selecting to be in my current virtual enviroment but i got it worked out. made a new one in programming? idk
- made model for user, thinking about trying to add feature where user selects favorite animal from game and then that animal is used more on their farm page. not sure where i would put the animal info in this project or if it should be a separate class. going into user_app admin and registering the model User. now i need to make migrations. went into proj on terminal. it says my database doesn't exist. capitalization matching error adjusted. looks good (i have to be in proj for migrations to work) now i want to enter the db. seems okay?
- now i want to run the server. doing so in main folder, jk that failed. okay now its up.  now i will go into the admin site. i will first create a superuser. Unique username: 'dalescape' , Character name: 'dal' , Password: '1234' (yelled at me but i bypassed it)  now going back to start the server, 
* Starting development server at http://127.0.0.1:8000/
* Admin site server and login here http:localhost:8000/admin
I can see Auth Tokens - Tokens, Authentication and Authorization - Groups, User_app - Users. Everything seems to be working well. 
- time to start working on the other models. but first i need to create a new file for data files. done. now i want to start creating data files. maybe start with animals in the game? see about apis and do a bit of research. then can move to include data from my spreadsheet. 
- added a json file with animal data, next would need to be crops? i cleaned up some data and added a json of crop data but its not perfect.
- i will push the current stuff rn before i start messing with the next models.


