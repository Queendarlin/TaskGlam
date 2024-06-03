# TaskGlam: A Flask-based Task Management App

## Introduction
TaskGlam is a web application designed to help you conquer your to-do list and stay organized. Built with Python Flask, it provides a user-friendly interface for registering, logging in, and managing tasks with features like:

* **User Management**: Create accounts, log in, and update account details.

* **Task Management**: Add tasks with titles, descriptions, due dates, and priorities (low, medium, high).

* **Task Editing and Deletion**: Edit and delete existing tasks to keep your list streamlined.
Task Completion: Mark tasks as complete for a satisfying sense of accomplishment.

* **Task Listing**: View all created tasks with their details in one place.

## Inspiration and Challenges
TaskGlam was born from the constant struggle to stay on top of things in a busy world. Juggling multiple tasks can be overwhelming, and I wanted to create a simple yet effective tool to manage them. The main challenges involved implementing user authentication, database integration with SQLite, and ensuring a smooth user experience across different functionalities.

## Technical Details
* **Backend:** Python Flask handles server-side logic, user authentication, and database interactions with SQLite.

* **Frontend:** HTML templates with CSS and Bootstrap provide the user interface and visual design.
* JavaScript: Used for basic user interactions and dynamic elements on the frontend.

* **Deployment:** Render.com provides a platform for deploying the application, making it accessible online.

## Struggles
TaskGlam represents a significant milestone for me as it's my first-ever web application project. Diving into development from scratch meant spending a lot of time learning and exploring new concepts. I had to exhaust many tutorials, experiment with code, and consult various resources to grasp the necessary skills. While challenging, this process was incredibly rewarding, solidifying my understanding of web development fundamentals.

Making the app visually appealing proved to be the most challenging aspect, as it is of paramount importance. There's always room for growth!

## Author
[**Queendarlin Nnamani**](https://www.linkedin.com/in/queendarlin-nnamani/)

See it in Action!
Access the deployed TaskGlam application here: [https://taskglamapp.onrender.com]

## Installation (Developers Only):

### Steps
* Clone this repository:
```Bash
git clone https://github.com/Queendarlin/TaskGlam.git
```
* Navigate to the project directory:
```Bash
cd TaskGlam
```
* Install required dependencies:
```Bash
pip install -r requirements.txt
```
* Create a .env file in the project root directory and configure environment variables for database connection and secret key.

* Run the application:
```Bash
python app.py
```
This will start the Flask development server, allowing you to access the application at http://127.0.0.1:5000/ (default port).

## Usage
* **Registration:** Create a new user account by visiting the signup page.

* **Login:** Existing users can log in with their credentials.

* **Task Management:** Add, prioritize, set due dates, edit, delete, and mark tasks as complete through the provided interface.

## Contributing:
Feel free to fork this repository and contribute to the project's development. Please create pull requests with clear descriptions of any changes.

Related Projects:
* Todoist (https://todoist.com/)
* TickTick (https://ticktick.com/?language=en_US)
* Asana (https://asana.com/)

Licensing:
This project is licensed under the MIT License.
MIT License

Copyright (c) 2024 [Queendarlin Nnamani]
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Visuals
* Add task view:
![Add-task](https://github.com/Queendarlin/TaskGlam/assets/112155127/6cc6fbed-c743-4205-8459-cba81fe9744e)


* Edit task view:
![edt-task](https://github.com/Queendarlin/TaskGlam/assets/112155127/2e650d0c-a1e8-4a5c-867a-710af9ece4b8)


* Delete task view:
![Detete-task](https://github.com/Queendarlin/TaskGlam/assets/112155127/ebe7e224-ace6-4c96-afd7-0ac275694f5a)


* Mark Task as complete:
![complete-task](https://github.com/Queendarlin/TaskGlam/assets/112155127/ca4ecb2f-34f9-4fa4-9fc1-20db414eb6c7)



