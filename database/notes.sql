-- This is the model for database
BEGIN TRANSACTION;
DROP TABLE IF EXISTS "notes";
CREATE TABLE IF NOT EXISTS "notes" (
	"id"	integer,
	"day"	varchar(20) NOT NULL,
	"month"	varchar(20) NOT NULL,
	"year"	varchar(30) NOT NULL,
	"content"	text NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
COMMIT;