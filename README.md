**Clone repository and installing virtual environment:** 
- Open terminal and run the following code one by one :
```
git clone https://github.com/Tushar-04/Athena.git
```

- If virtualenv not installed in your system :

```
pip install virtualenv
```
2. **Running virtual environment:**

```
cd .\Athena\
```

```
virtualenv venv
```
- Following code will enable virtual environment
```
.\venv\Scripts\activate
```
- Note: If you get any errors in the above command, run the following command in powershell as admin, else move to the next step.
```
Set-ExecutionPolicy RemoteSigned
```

3. **Instaling dependencies:**

```
pip install -r requirements.txt
```

4. **Now you can run the backend using following comand:**

```
py .\app.py
```