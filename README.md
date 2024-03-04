# Capstone Project: Movie Recommendation Engine

## Project Overview
This capstone project focuses on developing a Movie Recommendation Engine. It is a web application that suggests movies to users based on their preferences and ratings of previously watched movies. 
Using both content-based and collaborative filtering algorithms, the application delivers personalized movie recommendations.

## Key Features
- **User Authentication**: SignIn and SignUp functionalities.
- **Recommendation Engine**: Implements content-based and collaborative filtering for personalized suggestions.
- **User Profile Management**: Allows users to update their movie interests and ratings.
- **Responsive Design**: Utilizes Bootstrap, HTML, CSS, and Jinja2 for a responsive web interface.

## Tools and Technologies Used
- **Flask Framework**: For the web application's backend.
- **MySQL Database**: For storing user data and movie information.
- **Docker**: For containerizing the application and ensuring consistent environments.
- **Jenkins**: For automating Docker image building and updating the database.
- **PyUnitTest**: For unit testing of the application.
- **Jinja2**: Template engine for rendering the frontend of the application.
- **PyCharm**: Integrated Development Environment (IDE) used for application development.
- **GitHub**: Hosts the project repository for version control and collaboration.
- **PyBuilder**: Manages the build process for Python projects.

## Project Setup
This project was developed using Flask and deployed using Docker. The recommendation algorithms update movie suggestions every 15 minutes, 
ensuring that the database is always up to date with the latest recommendations.

## Testing
The application's functionality was verified using PyUnitTest. Integration with Jenkins allowed for continuous building and deployment of the Docker Image.

## Project Links
- GitHub Repository: [MovieRecommendationEngine](https://github.com/lokesh-venkata-sai/MovieRecommendationEngine)
- Docker Images: [Movie Recommendation](https://hub.docker.com/r/sreekarreddy2307/movie_recommendation), [SQL Container](https://hub.docker.com/r/sreekarreddy2307/sql-container)

## Learning Outcomes
- Developed proficiency in Flask, MySQL, Git, Docker, Jenkins, PyBuilder, and unit testing.

## Challenges Encountered
- Selection of efficient recommendation techniques.
- Collection of a comprehensive dataset.
- Deployment challenges with Docker and Jenkins integration.

This project lays the foundation for further enhancements and potentially serves as a stepping stone for future capstone projects.
