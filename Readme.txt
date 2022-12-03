Project Structure

//----------------------------PROJECT STRUCTURE---------------------------------
|_backend
	|_models
		|_sql_files
	|_view
		|_streamlit_views
	|_controller
		|_python functions which execute SQL statements
|_frontend


//-----------------------------HOW TO EXECUTE------------------------------------

1. RUN schema files in models(sql) to create schema and database
2. RUN stored-procedure & trigger sql files to store the respective entities
3. START streamlit server by executing py -m streamlit run app.py
4. EXPERIENCE application