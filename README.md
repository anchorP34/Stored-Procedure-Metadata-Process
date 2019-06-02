# Stored-Procedure-Metadata-Process
Creates a Stored Procedure Metadata Process For Update Statements

You can see the walkthrough video here: 

# FinalProcess.py
This python file looks at the stored procedure, finds the different locations for update statements, and then breaks it down for insert statements into a metadata table.

# Process.sql
This is the sample stored procedure that has 3 update statements that need to be extracted and broken down

# ProcessTable.sql
This is the metadata table that the FinalProcess.py script is trying to create insert statements for
