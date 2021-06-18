# [One Minute Pitch]

## By Carolyne Wanzuu

## Description

One minute Pitch is a web appliction that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

The pitches are organized by category. You can have different categories like pickup lines, interview pitch, product pitch, promotion pitch.

With the application, a user will be able to:

* See various pitch categories and select the ones they prefer.
* Sign in and create new pitches
* Like or dislike a pitch

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display pitches | **On page load** | List of various pitches category |
**On signing in** | create a new pitch|
| Display pitches created within your profile page | **On page load** | view pitches created |
| like or dislike a pitch| **Signing out** |displays the home page  |

### Prerequisites

You need the following to start working on the project on your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.8
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone this repository to your local computer.
* Ensure you have python3.8 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual amchine.

* Create start.sh file and in it write the following lines:
```
 export SECRET_KEY='<Your-secret-Key>'
 python3.8 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* Alternatively the application can be accessed by visiting https://git.heroku.com/pitches0.git

## Technologies Used

* Python v3.8
* Boostrap
* Flask


## License

MIT License

Copyright (c) 2021 Carol Wanzuu