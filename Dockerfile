FROM nikolaik/python-nodejs:python3.7-nodejs10

COPY . /root/project25/

WORKDIR /root/project25

RUN pip install numpy scipy matplotlib \
    && npm install \
    && bower install

EXPOSE 3000

CMD ["sh", "-c", "npm start"]