##End Points
+ `api/v1.0/signup/`

 - **POST** 

 > curl -H "Content-type: application/json" -d "{"username":`<username>`,"password":`<password>`}"

+ `api/v1.0/o/token/`
 
 - **POST** 

 > curl -X POST -d "grant_type=password& username=`<username>` & password=`<password>`" https://`<client_id>`:`<client_secret>`@catfarm.herokuapp.com/api/v1.0/o/token/

+ `api/v1.0/cats`

 - **GET**
 
 > curl -H "Authorization: Bearer `<token>`" https://catfarm.herokuapp.com/api/v1.0/cats/

 - **POST**

 > curl -X POST -H "Authorization: Bearer `<token>`" 
-H "Content-type: application/json"
-d "{`...`}" https://catfarm.herokuapp.com/api/v1.0/cats/


+ `api/v1.0/cats/<id>/`

 - **GET**
 
 > curl -H "Authorization: Bearer `<token>`" https://catfarm.herokuapp.com/api/v1.0/cats/`<id>`/

 - **PUT/PATCH**

 > curl -X `<PUT/PATCH>` -H "Authorization: Bearer `<token>`"
-H "Content-type: application/json"
-d "{`...`}" https://catfarm.herokuapp.com/api/v1.0/cats/`<id>`/

 - **DELETE**  

 >curl -X DELETE -H "Authorization: Bearer `<token>`" https://catfarm.herokuapp.com/api/v1.0/cats/`<id>`/


##Cat
   
    {  
        "name": CharField,  
        "breed": CharField,
        "age": IntegerField,
        "hairiness": CharField, choices (s, m , l)
    } 