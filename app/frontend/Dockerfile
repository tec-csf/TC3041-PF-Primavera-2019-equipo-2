# Using lightweight alpine image
FROM python:3.6-alpine

# Installing packages
RUN apk update

# Defining working directory and adding source code
WORKDIR /usr/src/frontend
COPY requirements.txt ./

# Install API dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Exportar la variable de entorno FLASK_APP apuntando al ejecutable
ENV FLASK_APP=frontend.py

# Add application code.
COPY . ./

# Start app
#CMD [ "python", "./frontend.py" ]

# Start app
EXPOSE 8080
CMD [ "flask", "run", "--host=0.0.0.0" ]
