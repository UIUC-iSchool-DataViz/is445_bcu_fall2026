---
title: Lecture 5.2 - GitHub Pages Setup
layout: lecture
description: >-
 Getting set up with a github.io account
date: 2025-09-29
---


<br />
<br />
<br />

# TOPIC 2: Getting setup with github.io

---

## github.io for publishing

Step 1: Create/login to your github account

notes:
(We'll also do this "live" in the coding section of class)

---

## github.io for publishing

Step 2: Create new repository

<img src="images/githubSetup/githubio1.png" width="800" alt="A screenshot of the Prof's landing page for github.com.">

---

## github.io for publishing

Step 2: Create new repository

<img src="images/githubSetup/githubio1_nm.png" width="800" alt="A screenshot of the Prof's landing page for github.com with the 'New' button for creating a new repository highlighted.">

---

## github.io for publishing

Step 3: Name your new repository as ```[username].github.io```

<img src="images/githubSetup/githubio2_nm.png" width="800" alt="A screenshot of how to create a new github.io page (in the screenshot it is for 'jnaiman.github.io').">

---

## github.io for publishing

Step 3: Name your new repository as ```[username].github.io```

<img src="images/githubSetup/githubio2.png" width="800" alt="A screenshot of how to create a new github.io page (in the screenshot it is for 'jnaiman.github.io') with the name of the repository highlighted.">

notes: the name is important here!!

---

## github.io for publishing

Step 4: Clone your repository

<img src="images/githubSetup/githubio3_nm.png" width="800" alt="Screenshot of default page for a new, but empty repository on github.">

---

## github.io for publishing

Step 4: Clone your repository

<img src="images/githubSetup/githubio3.png" width="800" alt="Screenshot of default page for a new, but empty repository on github with the URL to copy to clone the repo with 'git clone' on a local machine.">

notes: make note of your git name, we'll use this for "cloning" our github repo

---

## github.io for publishing

Step 5: Clone your repository
 * In command line do: ```git clone YOUR_REPO_LINK```

---

## github.io for publishing

Step 5: Clone your repository
 * In command line do: ```git clone YOUR_REPO_LINK```

 #### You might be prompted to add in your credentials:

<img src="images/githubSetup/stackoverflow.png" alt="Image shows prompts to set global 'git config' for user email and name.  Original URL for image: https://stackoverflow.com/questions/65257503/cannot-commit-when-i-had-created-a-file-using-git"/>

---

## github.io for publishing

Step 5: Clone your repository
 * In command line do: ```git clone YOUR_REPO_LINK```

 #### You might be prompted to add in your credentials:

<img src="images/githubSetup/stackoverflow.png" alt="Image shows prompts to set global 'git config' for user email and name.  Original URL for image: https://stackoverflow.com/questions/65257503/cannot-commit-when-i-had-created-a-file-using-git" width=400/>

See instructions for [setting up your credentials in Git](https://docs.github.com/en/get-started/getting-started-with-git/setting-your-username-in-git).


---

## github.io for publishing

Step 6: In the command line, move into your github.io folder with 
 * ```cd <GITHUB USER NAME>.github.io```

**Be aware:** you might have to put a full path to "cd" into like 
 * ```cd /Users/jillnaiman/jnaiman.github.io```

---

## github.io for publishing

Step 6: In the command line, move into your github.io folder with 
 * `cd <GITHUB USER NAME>.github.io`

Be aware: you might have to put a full path to "cd" into like 
 * `cd /Users/jillnaiman/jnaiman.github.io`

Step 7: Add an `index.html` file to this new folder (download via the link in Lab \#4).


---

## github.io for publishing

Step 8: Add files to your repo officially
 * ```git add -A```
 
Step 9: Commit these files (say what you are doing)
 * ```git commit -m "my first add"```
 
Step 10: Push to your online repo
 * ```git push```
 
Step 11: wait for your website to build and then check it out!
 * Link: ```https://YOUR_GITHUB_USER_NAME.github.io/```


---

## github.io for publishing

Step 8: Add files to your repo officially
 * ```git add -A```
 
Step 9: Commit these files (say what you are doing)
 * ```git commit -m "my first add"```
 
Step 10: Push to your online repo
 * ```git push```
 
Step 11: wait for your website to build and then check it out!
 * Link: ```https://YOUR_GITHUB_USER_NAME.github.io/```
 
**You can use GUI interface, but later you'll need the command line!**

<!--

An example from a DPI talk Prof. Turk and I gave [can be found right here](https://mediaspace.illinois.edu/media/t/1_a874v3q7).
-->

notes:
you can also use the GUI interface to do this if you are more comfortable with that, but you'll need to use the command line later so best to start with that

---

## github.io for publishing

<img src="images/githubSetup/github_labsetup_1.png" width=500 alt="Screenshot of prompt for Lab \#4 on PrairieLearn with the 'Enter URL here:' section highlighted.">

notes:
you'll get some feedback instantaneously as well as your grade

---

## github.io for publishing

We will be storing time/hash information upon your submission:

<img src="images/githubSetup/checksum_github.png" alt="Screenshot of feedback from a successful submission of your github.io page with the information about your submission date and time and the hash we'll be using for grading.">

notes:
On successful submission you'll see something like the following -- for the purposes of this lab, as long as you get a 100%, you are good to go, but the format of the output is something you'll see come up again for submissions that involve a URL.  

For grading, we will only be looking at submissions marked before the due date on your repo, so be sure to get in all changes you want to submissions before the due date!

---

## github.io for publishing

<img src="images/githubSetup/github_labsetup_2.png" width=500 alt="Screenshot of prompt for Lab \#4 on PrairieLearn with an emphasis on making sure to use the index.html file that is linked on the lab prompt.">

notes:
one final thing -- be sure you use the index.html file linked here in your lab instance!


---

## More info:

[https://pages.github.com/](https://pages.github.com/)


---

## Some things to keep in mind

 * You might have to set up a personal access token, see: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
 * You might have to specify a "branch" to build from: on your github.io code page go to Settings -> Pages and select "Branch:master"/"Branch:main" under "Source"

<img src="images/githubSetup/set_branch.png" width="700px" alt="Screenshot of clicking on 'Settings' on your github repository, selecting 'Pages' from the left side bar, and clicking on 'master' or 'main' from the dropdown menu under the 'Source' heading.  This is necessary to specify you are building your page from a branch.">


---

## Next week -- "flipped" class for Lab \#5

In particular, I am assuming you have watched the [Part 2 Video](https://mediaspace.illinois.edu/media/t/1_k93hei8q) already before joining the class next week (video on Module page) *and* have looked at the prep notebook in Week 6.

**We will spend the majority of class next week with time to work on Lab \#5.**

**(Yes, this is a hint that Lab \#5 is a tough one!)**

notes:
this is just a reminder!

---

# To Python for more interactivity!

---
