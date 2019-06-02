
# First Read in the File and print it out to the terminal
all_lines = []
with open('Process.sql','r') as f:
    for line in f.readlines():
        all_lines.append(line)
        #print(line)

clean_lines = []
for line in all_lines:
    if line.strip().startswith('--'):
        pass
    else:
        clean_lines.append(line.replace('\n',''))

# Find the Udpate Statment Locations
update_locations = []
for idx, line in enumerate(clean_lines):
    if line.upper().strip().startswith('UPDATE'):
        update_locations.append(idx)

for i in range(len(update_locations)):
    print('---------------------------')
    print('-------UPDATE SECTION------')
    print('---------------------------')
    print('\n')
    try:
        full_statement = " ".join(clean_lines[update_locations[i]:update_locations[i+1]])
    except IndexError:
        full_statement = " ".join(clean_lines[update_locations[i]:]).replace('END GO','')
    print('/*',full_statement.strip(),'*/')

    # Get Information
    update_table = " ".join(full_statement.split('FROM ')[1].split()[0:2])
    update_columns = full_statement.split('SET ')[1].split('FROM')[0]

    update_joins = full_statement.split('FROM ')[1].split('WHERE')[0].replace(update_table, '').strip()
    
    where_clause = full_statement.split(' WHERE ')[1]

    print('\n/* Update Table: {} */\n'.format(update_table))
    print('\n/* Update Columns: {} */\n'.format(update_columns))
    print('\n/* Update Joins: {} */\n'.format(update_joins))
    print('\n/* WHERE Clause: {} */\n'.format(where_clause))
    
    #INSERT STATEMENT
    print('INSERT INTO dbo.ProcessTable')
    print('VALUES')
    print('(')
    print("\t  '{}' -- Update Table".format(update_table))
    print("\t, '{}' -- Update Columns".format(update_columns.replace("'","''").strip()))
    print("\t, '{}' -- Update Joins".format(update_joins.replace("'","''").strip()))
    print("\t, '{}' -- Where Clause".format(where_clause.replace("'","''").strip()))
    print(');')
    print('\n')