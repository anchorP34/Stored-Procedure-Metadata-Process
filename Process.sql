CREATE PROCEDURE dbo.PROCESS
AS

BEGIN

    -- Update Statement1
    UPDATE sports
    SET SportName = 'Baseball'
    FROM dbo.Sports sports
    WHERE sports.PlayedOutside = 1
    AND sports.BallColor = 'White'
    AND sports.Season = 'Summer'

    -- Update Statement2
    UPDATE sports
    SET SportName = 'Basketball'
    FROM dbo.Sports sports
    WHERE sports.PlayedOutside = 0
    AND sports.BallColor = 'Orange'
    AND sports.Season = 'Winter'
    
    -- Update Statement With Joins
    UPDATE a 
    SET ColumnX = b.Column3 
    FROM dbo.TableA a 
    JOIN dbo.TableB b on a.CommonColumnID = b.CommonColumnID 
    LEFT JOIN dbo.TableC on c.Column4 = b.Column4
    WHERE c.PrimaryKey IS NULL
    AND a.Column8 = 'Tuesday'


END
GO