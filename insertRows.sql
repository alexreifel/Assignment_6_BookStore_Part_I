PRAGMA foreign_keys = ON;

INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Classic Sci-Fi', 'classic-scifi-category.jpg'),
(2, 'Cyberpunk', 'cyberpunk-category.jpg'),
(3, 'Space Opera', 'space-opera-category.jpg'),
(4, 'Hard Science Fiction', 'hard-scifi-category.jpg');

INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'Foundation', 'Isaac Asimov', '9780553293357', 14.99, 'foundation.jpg', 1),
(2, 1, 'Dune', 'Frank Herbert', '9780441013593', 18.99, 'dune.jpg', 1),
(3, 1, 'The Left Hand of Darkness', 'Ursula K. Le Guin', '9780441478125', 15.99, 'left-hand.jpg', 0),
(4, 1, 'Do Androids Dream of Electric Sheep', 'Philip K. Dick', '9780345404473', 13.99, 'androids.jpg', 1),
(5, 2, 'Neuromancer', 'William Gibson', '9780441569595', 15.99, 'neuromancer.jpg', 1),
(6, 2, 'Snow Crash', 'Neal Stephenson', '9780553380958', 17.99, 'snow-crash.jpg', 1),
(7, 2, 'Burning Chrome', 'William Gibson', '9780060539825', 13.99, 'burning-chrome.jpg', 0),
(8, 2, 'Rainbows End', 'Vernor Vinge', '9780812536362', 14.99, 'rainbows-end.jpg', 0),
(9, 3, 'A Fire Upon the Deep', 'Vernor Vinge', '9780812515282', 16.99, 'fire-upon-deep.jpg', 0),
(10, 3, 'Revelation Space', 'Alastair Reynolds', '9780441009176', 17.99, 'revelation-space.jpg', 0),
(11, 3, 'The Player of Games', 'Iain M. Banks', '9780316005401', 15.99, 'player-of-games.jpg', 1),
(12, 3, 'Hyperion', 'Dan Simmons', '9780553283686', 16.99, 'hyperion.jpg', 1),
(13, 4, 'The Martian', 'Andy Weir', '9780553418026', 15.99, 'martian.jpg', 1),
(14, 4, 'Blindsight', 'Peter Watts', '9780765319647', 16.99, 'blindsight.jpg', 0),
(15, 4, 'Seveneves', 'Neal Stephenson', '9780062190376', 19.99, 'seveneves.jpg', 0),
(16, 4, 'Diaspora', 'Greg Egan', '9780575082076', 17.99, 'diaspora.jpg', 0)

