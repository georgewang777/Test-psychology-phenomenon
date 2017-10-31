# -*- coding: cp936 -*-
import media13
import fresh_tomatoes

Mountains_May_Depart = media13.Movie("Mountains May Depart",
                                     "a story about Time and Love",
                        "https://upload.wikimedia.org/wikipedia/zh/3/35/Mountains_May_Depart.jpg",
                        "https://www.youtube.com/watch?v=qc1ZKyhMG6o"
                        )

Dangal = media13.Movie("Dangal",
                       "based on the story of Mahavir Singh Phogat, an amateur wrestler, who trains his daughters Geeta Phogat and Babita Kumari to be world-class wrestlers ",
                       "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
                       "https://www.youtube.com/watch?v=x_7YlGv9u1g")

Wolf_Warriors2 = media13.Movie("Wolf Warriors2",
                               "The film tells a story of a loose cannon Chinese soldier named Leng Feng who takes on special missions around the world",
                               "https://upload.wikimedia.org/wikipedia/en/b/b5/Wolf_Warriors_2_poster.jpeg",
                               "https://www.youtube.com/watch?v=fkqGiPB2D8M")

Shawshank = media13.Movie("the shawshank redemption",
                           "The film tells the story of banker Andy Dufresne (Tim Robbins), who is sentenced to life in Shawshank State Penitentiary for the murder of his wife and her lover, despite his claims of innocence ",
                          "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                           "https://www.youtube.com/watch?v=6hB3S9bIaco")

Bullets_Fly = media13.Movie("Let The Bullets Fly",
                            "The film is set in Sichuan during the 1920s when the bandit Zhang (Jiang Wen) descends upon a town posing as its new governor",
                            "https://upload.wikimedia.org/wikipedia/id/b/b3/Let_the_Bullets_Fly.jpg",
                            "https://www.youtube.com/watch?v=rpGwgImqaX4")

Forrest = media13.Movie("forrest gump",
                     "The story depicts several decades in the life of Forrest Gump, a slow-witted but kind-hearted, good-natured and athletically prodigious man from Alabama, who witnesses, and in some cases influences, some of the defining events of the latter half of the 20th century in the United States",
                      "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                      "https://www.youtube.com/watch?v=YNh9Es8Ut6U")
movies = [Mountains_May_Depart,Dangal,Wolf_Warriors2,Shawshank,Bullets_Fly,Forrest]
fresh_tomatoes.open_movies_page(movies)
