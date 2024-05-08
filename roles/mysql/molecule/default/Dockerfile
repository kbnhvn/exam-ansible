# Use Ubuntu 20.04
FROM ubuntu:20.04

# Update and install tools
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y net-tools iputils-ping sudo apt-utils

# Install Python 3.8
RUN apt-get install -y python3.8

# Install mysql-server
RUN apt-get install -y mysql-server mysql-client

# Copy conf
COPY ./files/my.cnf /root/.my.cnf

# Start mysql
RUN systemctl start mysql

# Définir l'interpréteur Python par défaut
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Nettoyer le cache des paquets pour réduire la taille de l'image
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Commande par défaut à exécuter lorsque le conteneur démarre
CMD ["/bin/bash"]