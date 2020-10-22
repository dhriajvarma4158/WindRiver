# WindRiver
Solution Proposed:

Return Python code using flask and created all the three apis

1. http://18.221.197.38:5000/health -- This is giving simple response (Working from browser)

2. http://18.221.197.38:5000/api/encrypt -- This is POST API and requires JSON as an input, so please use curl of POSTMAN to validate the response

3. http://18.221.197.38:5000/api/decrypt -- This is POST API and requires JSON as an input, so please use curl of POSTMAN to validate the response

Please note:

As everytime new key is being generated so response of encryption and decryption will differ.

So kindly ensure to use encryption API first and than second API first

We can also just generate key once and use it in code entirely, but that would have made things tad less secure.


Sample Response Output

curl -X POST  http://18.221.197.38:5000/api/encrypt -d '{"Input": "Hello World"}' -H 'Content-Type: application/json'                           {
  "Input": "Hello World",
  "Output": "gAAAAABfkYR8vvBjgi23MIy5hP-xu-WO26OAdquycsUbIBX1BdYRe117SwQJv1-T50WyVLePyqMwSibaEplUaZxRHoY8nZxCAA==",
  "Status": "success",
  "Message": ""
}
root@ip-172-31-45-50:~# curl -X POST  http://18.221.197.38:5000/api/decrypt -d '{"Input": "gAAAAABfkYR8vvBjgi23MIy5hP-xu-WO26OAdquycsUbIBX1BdYRe117SwQJv1-

T50WyVLePyqMwSibaEplUaZxRHoY8nZxCAA=="}' -H 'Content-Type: application/json'
{
  "Input": "gAAAAABfkYR8vvBjgi23MIy5hP-xu-WO26OAdquycsUbIBX1BdYRe117SwQJv1-T50WyVLePyqMwSibaEplUaZxRHoY8nZxCAA==",
  "Output": "Hello World",
  "Status": "success",
  "Message": ""
}



4. It is containerized using Dockerfile code which is attached.

5. Run the command to create image, please ensure docker is installed and service is running

docker build -t viapythonimage . (. represents the current directory)

6. Run following command to create container using the image

 docker run -t -i -d -p 5000:5000 viapythonimage

7.  Access the application url on http://<instanceip>:5000/health
In my case it is http://18.221.197.38:5000/health

