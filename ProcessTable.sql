CREATE TABLE dbo.ProcessTable
(
    PK int identity(1,1) PRIMARY KEY
    , UpdateTable nvarchar(255)
    , UpdateColumns nvarchar(255)
    , UpdateJoins nvarchar(255)
    , WhereClause nvarchar(max)
)