# What order was the most expensive? Which one was the cheapest?
# The most expensive:

chinook.pretty_print("""
                    SELECT MAX(Invoice.Total), *
                    FROM Invoice;
                    """)

#  Which one was the cheapest?

chinook.pretty_print("""
                    SELECT MIN(Invoice.Total), *
                    FROM Invoice;
                    """)

# Which city had the most orders?

chinook.pretty_print("""
                    SELECT Invoice.BillingCity, COUNT(*) AS Invoice_num
                    FROM Invoice
                    GROUP BY Invoice.BillingCity
                    ORDER BY Invoice_num DESC;
                    """)

# c) Calculate (or count) how many tracks have this MediaType: Protected AAC audio file.

# Solution 1)

chinook.pretty_print("""
                    SELECT COUNT(*)
                    FROM Track
                    JOIN MediaType ON Track.MediaTypeId=MediaType.MediaTypeId
                    WHERE MediaType.Name='Protected AAC audio file';
                    """)
# Solution 2)

chinook.pretty_print("""
                    SELECT MediaType.Name, COUNT(*)
                    FROM Track
                    JOIN MediaType ON MediaType.MediaTypeId = Track.MediaTypeId
                    GROUP BY Track.MediaTypeId;
                    """)

# d) Find out what Artist has the most albums?
# Solution 1)

chinook.pretty_print("""
                    SELECT Artist.Name, COUNT(*) as Album_num
                    FROM Artist
                    JOIN Album ON Album.ArtistId = Artist.ArtistId
                    GROUP BY Album.ArtistId
                    ORDER BY Album_num DESC;
                    """)

# Solution 2)

chinook.pretty_print("""SELECT COUNT(Artist.Name) AS Alb_count, Artist.Name AS Art_name 
                    FROM Artist
                    INNER JOIN Album ON Album.ArtistId=Artist.ArtistId
                    GROUP BY Artist.ArtistId
                    ORDER BY -COUNT(Artist.Name)""")

# e) What genre has the most tracks?

chinook.pretty_print("""
                    SELECT Genre.Name, COUNT(*) as Track_num
                    FROM Genre
                    JOIN Track ON Track.GenreId = Genre.GenreId
                    GROUP BY Track.GenreId
                    ORDER BY Track_num DESC;
                    """)
# f) Which customer spent the most money so far?

chinook.pretty_print("""
                    SELECT Customer.FirstName, Customer.LastName, SUM(Invoice.Total) AS Invoice_sum
                    FROM Customer
                    JOIN Invoice ON Invoice.CustomerId = Customer.CustomerId
                    GROUP BY Invoice.CustomerId
                    ORDER BY Invoice_sum DESC;
                    """)

# g) What songs were bought with each order?
# (hint: here you have to do a many-to-many SQL
# query with three tables: Track, Invoice and InvoiceLine.
# You have to do two JOINS here)

chinook.pretty_print("""
                    SELECT Invoice.InvoiceId, Track.Name
                    FROM Invoice
                    JOIN InvoiceLine ON InvoiceLine.InvoiceId = Invoice.InvoiceId
                    JOIN Track ON InvoiceLine.TrackId = Track.TrackId;
                    """)

























