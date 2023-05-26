SELECT Movie.MID as “MID”,
Movie.title as “Film Adı”,
Movie.year as “Çekim Yılı”,
Location.Name as “Çekildiği Yer”
FROM Movie 
JOIN M_Location ON Movie.MID = M_Location.MID 
JOIN Location ON M_Location=LID=Location.LID
