<h3><b>Build the image</b></h3>
<ul>
<li>$: docker build -t sreekar/app . -f Dockerfile</li>
<li>$: docker build -t mysql-image . -f Dockerfile2</li>
</ul>
<h3><b>Create the network</b></h3>
<ul>
<li>$: docker network create mynetwork</li>
</ul>
<h3><b>Run the Container</b></h3>
<ul>
<li>$: docker run -d --name mysql-server --network mynetwork -e MYSQL_ROOT_PASSWORD=lokesh1999 mysql-image</li>
<li>$: docker run -it --network mynetwork --name webapplication -p 3000:5000 sreekar/app</li>
</ul>
<h3>Use the application</h3>
<ul>
<li>$: curl localhost:8080</li>
</ul>
<h3><b>link local image and repository</b></h3>
<ul>
<li>$:docker tag local-image:tagname username/new-repo:tagname </li>
</ul>
<h3><b>Pull & Push image from docker hub</b></h3>
<ul>
<li>$:docker push sreekarreddy2307/movie_recommendation:latest</li>
<li>$:docker push sreekarreddy2307/sql-container:latest</li>
<li>$:docker pull sreekarreddy2307/movie_recommendation:latest</li>
<li>$:docker pull sreekarreddy2307/sql-container:latest</li>
</ul>
<h3><b>Use the Application on browser</b></h3>
<ul><li>Can access on 192.168.99.100:3000</li></ul>
<h3>In case if docker-compose is used</h3>
<ul><li>$:docker-compose up --build</li>
<li>$:curl localhost:3000</li></ul>
