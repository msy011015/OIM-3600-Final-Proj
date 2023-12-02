# OIM 3600 Final Proj - Jenny Ma
This is a repository for Jenny's Wonderful Traveling Web App.

## 1. Project Overview

The Traveling WebApp is an innovative platform designed to enhance travelers' experiences by simplifying the process of discovering and researching locations. The core feature of this web application is its user-friendly search engine, enabling users to input keywords related to their desired destinations. Additionally, users can specify the type of location they are interested in, such as "hotels," "attractions," "restaurants," or "geos," to refine their search results. Once a search is initiated, the webapp retrieves up to 10 relevant locations along with their addresses. Further details, including contact information, descriptions, ratings, rankings, and even opening hours when applicable, are easily accessible by clicking on a location's name. Users can also seamlessly explore more information on TripAdvisor by the external link provided directly. Further information, including awards, reviews, photos, and nearby locations, is listed in the following sections. The Traveling WebApp aims to provide travelers with comprehensive information and a streamlined interface to make informed decisions and enhance their travel experiences.

## 2. Usage Guidelines

To maximize the benefits of the WebApp, users should begin by entering relevant keywords. It is optional to select a desired category of location, but will help generate more accurate and tailored search results. Users can click on the location's name to access detailed information, including contact details, descriptions, ratings, rankings, and opening hours if applicable. Additionally, the "Explore More on TripAdvisor" button provides a convenient way to access further insights. Users can also check the information of awards, reviews, photos, and nearby locations. The webapp is designed to be intuitive and user-friendly, making it easy for travelers to research their interested location in the trip.

## 3. Dependencies

The Traveling WebApp relies on HTML, CSS, and JavaScript for its frontend, with the user interface benefiting from Bootstrap templates.The template is utilized for frontend design, providing responsive templates and styling to enhance the user interface. Flask, a Python web framework, powers the backend, handling user requests and database interactions. TripAdvisor API is the base of the app and enriched the location data. The related Python script for extracting data from the TripAdvisor API relies on the 'requests' library to communicate with the API and retrieve location information. Such technologies stack ensures a responsive and feature-rich platform for travelers.

## 4. Project Structure

The Traveling WebApp is organized into a clear and structured project directory, ensuring efficient development and maintenance. The primary components include:

- **Main Directory:**
    - **app.py:** This is the main Python script that serves as the entry point for the Flask application. It handles routing, views, and communication with the frontend.
    - **templates:** This directory contains HTML templates, including index.html, location_list.html, location_details.html, and contact.html, for rendering webpages using Flask's template engine. It's where the user interface layout and structure are defined.
    - **static:** The 'static' directory stores static assets including CSS files, JavaScript scripts, and images. These files enhance the user experience by providing styling and interactivity.

- **API:**
    - The 'trip_helper.py' contains Python scripts responsible for interacting with the TripAdvisor API. This includes functions to send requests, retrieve data, and process responses from the API.

This organized structure ensures that different aspects of your Traveling WebApp, from the frontend templates and styling to the backend logic and external API integration, are neatly separated and easily manageable. It promotes scalability and makes it straightforward to maintain and expand your web application.

## 5. Acknowledgments

I would like to extend our appreciation to the following:

- **Requests Library:** Thanks to the open-source 'requests' library, which played a pivotal role in making HTTP requests to the TripAdvisor API, simplifying data retrieval and integration.

- **TripAdvisor API:** Thanks to the TripAdvisor API, which provided invaluable location data, detailed information and other essential insights. This API was instrumental in enhancing the richness of our Traveling WebApp.

- **Bootstrap:** Thanks to the Bootstrap for its contributions to the frontend design of my web application. Bootstrap's responsive templates and styling have significantly improved the user interface, providing an aesthetically pleasing and user-friendly experience for travelers.

These contributions have been essential in the development of the Traveling WebApp, allowing me to create a feature-rich platform that simplifies travel research and decision-making for users around the world.

## 6. Reflection
The journey of creating the Traveling WebApp has been both challenging and rewarding. 

From the process point of view, extracting information using a Python API is remarkably smooth as this is a skill I've honed through my past studies. However, implementing a Bootstrap template presented challenges. Initially, I struggled with their complexity, particularly when integrating the CSS and other files into my webpage. Resolving this required creating static documents and modifying the template's original content based on tutorials I found. Furthermore, customizing the template proved difficult. The layout initially baffled me, but with extensive research and the addition of my own CSS for new sections, I began to understand and manipulate its structure more effectively.

A critical aspect of my process was thorough testing. For instance, I noticed that varying search results could cause display errors on the page, such as 'NoneType' errors when encountering addresses without contact details or opening hours. Continuous testing allowed me to identify and fix these issues. Looking ahead, I aspire to develop a database that allows users to view detailed information, mark favorites, and store them for convenient access. This, however, requires more time and deeper study to execute effectively.

From a learning perspective, I learned how to incorporate external APIs and quickly build a website using templates, a significant shift from my earlier assignments where I rarely used templates and spent much time adjusting the structure and design of the pages. This skill was valuable as it helped me understand the interaction between front-end and back-end in developing a complete web application.

One of the biggest lessons I learned was the importance of testing. Being naturally impatient and not fond of double-checking, I discovered during the testing phase that there were many aspects I had initially overlooked. Correcting these issues step by step through trial and error allowed me to refine the web app. This process taught me the necessity of patience and the importance of continuous improvement in any work, especially in software development where regular updates are crucial.

While ChatGPT was helpful, especially in assisting with the creation of this README.md by refining my ideas into more understandable and fluent language, its limitations became apparent in dealing with external APIs. ChatGPT couldn't access external sites or fully understand the specifics of my site. However, it provided valuable guidance in identifying and troubleshooting problems more efficiently. Reflecting on the entire project, I realized I had missed the instruction of "static" files in the guidelines, which would have made my work much smoother had I noticed and understood it earlier. Overall, the project was a significant learning experience in using and editing templates to establish a complete web app, as well as in effective project management.
