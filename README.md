
# Little Explorers - A Holiday Recommendation Website by Karen Samad

**** device image *****

Little Explorers is a user-friendly website dedicated to effortlessly browsing and recommending child-friendly holiday destinations. Searching through the recommendations is simplified with an intuitive filter mechanism. Users possess the capability to view, edit, and delete their recommendations effortlessly, while also having the convenience to contact the site's administrators for any inquiries. Furthermore, the site is fortified against malicious content through a "report a post" feature, enabling users to flag inappropriate content, which administrators can promptly review and remove as necessary.

This project is my third Milestone Project as part of the Code Institute's Diploma in Web Application Development. 

---

**** table of contents *****


---

## User Experience Design

### **Strategy Plane**

#### Site Goals

- To give users the opportunity to find child friendly holidays in the UK.

- To generate revenue from an integrated e-commerce site selling child-related holiday equipment. 

#### User Stories

1. As a user, I want to be able to:

    -  Find what I’m looking for on the site easily and intuitively from the home page and navigation bar. 
    - View the site any device and for the site to be responsive.
    - View and filter holiday recommendations posted by other users.
    - Contact the site owners to suggest a new holiday type, ask questions or report a malicious recommendation.
    - Return to the home page without having to use my browser buttons. including when I navigate to a non-existent page or I’m thrown an error.

2. As a user without an account, I want to be able to:

    - Understand the purpose of the site from the home page
    - Set up an account so I can create my own recommendations.

3. As a user with an account, I want to be able to:

    - Sign into my account.
    - Add my own holiday recommendation using a user-friendly form.
    - View my previously posted holiday recommendations.
    - Edit/Delete recommendations I have posted.
    - Comment on holiday recommendations, adding information about a holiday destination and verifying the post.
    - Log out of my account easily. 

4. As an administrator I want to be able to:

    - Sign into my account quickly and easily.
    - Edit any recommendation if necessary.
    - Add a new holiday type category.
    - Edit a new holiday type category.
    - Delete a user if necessary.
    - Receive email messages from the site users. 
    - Log out of my account easily. 

--- 

### **Scope Plane**

The following opportunity matrix summarises the key features that could be implemented on Little Explorers and the difficulty/viabitliy of each feature. The opportunities will be developed based on their priority scores.

#### **Table 1 Opportunity Summary**

| **Opportunity**                                                                               | **User**       | **Inportance** | **Viability** | **Score** |
|-----------------------------------------------------------------------------------------------|----------------|----------------|---------------|-----------|
| All pages - Navbar                                                                            | All            | 5              | 5             | 10        |
| All pages - Footer containing social links, contact, copyright and disclaimer                 | All            | 5              | 5             | 10        |
| Homepage - brand and explanatory text                                                         | All            | 5              | 5             | 10        |
| Homepage - Showcase of some recommendations                                                   | All            | 5              | 5             | 10        |
| Recommended holiday main page - Showcase of recommendations + Map showing holiday desinations | All            | 5              | 3             | 8         |
| Recommended holiday main page - Map with clickable links                                      | All            | 5              | 2             | 7         |
| Filter function to find tailored recommendations                                              | All            | 5              | 3             | 8         |
| Contact Page                                                                                  | All            | 5              | 5             | 10        |
| Sign In Functionality                                                                         | All            | 5              | 5             | 10        |
| Create Account Functionality                                                                  | All            | 5              | 5             | 10        |
| Sign Out Functionality                                                                        | Signed In User | 5              | 5             | 10        |
| Passowrd reset Functionalitliy                                                                | Signed In User | 3              | 1             | 4         |
| Profile Page with user's own recommendations + edit/delete options                            | Signed In User | 5              | 5             | 10        |
| User add Recommendation Page                                                                  | Signed In User | 5              | 5             | 10        |
| User edit Recommendation Page                                                                 | Signed In User | 5              | 5             | 10        |
| Holiday Recommendation Full Page information with map                                         | Signed In User | 5              | 4             | 9         |
| Ability to Report a Recommendation                                                            | Signed In User | 4              | 4             | 9         |
| Admin profile page with options to add/edit recommendations and holiday types                 | Admin Only     | 5              | 5             | 10        |
| Manage Holiday Type Page (with edit/delete links)                                             | Admin Only     | 5              | 5             | 10        |
| Add Holiday Type Page                                                                         | Admin Only     | 5              | 5             | 10        |
| Edit Holiday Type Page (with delete button)                                                   | Admin Only     | 5              | 5             | 10        |
| User search function                                                                          | Admin Only     | 4              | 3             | 7         |
| Delete user functionalitly                                                                    | Admin Only     | 4              | 4             | 8         |
| Custom Error Pages                                                                            | All            | 5              | 3             | 8         |

### Stucture Plane

Based on the [User Stories](README.md#user-stories) and the opportunities outlined in [Table 1](README.md#table-1-opportunity-summary) the following structure was planned for the site. 

This site map outlines the design of the website and which pages are accesible to which user. 

![site map](documentation/design_images/little_explorer_site_map.png)

This table outlines the design for the PostgreSQL database used to store the data, a relational database.

![database_design](documentation/design_images/holiday_database_outline.png)

## ?. Finished site
## ?. Technologies

### Languages

HTML, CSS, JavaScript & Python

### Frameworks, Libraries and Programs Used

* [LucidCharts](https://www.lucidchart.com) - To produce the site flow chart and database design.
* [TableConvert](https://tableconvert.com/csv-to-markdown)- For simplifying the writing of Markdown tables,


## ?. Testing
## ?. Deployment
## ?. Credits


## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

------


