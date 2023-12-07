# DOCFILE ABOUT API

## Gather funtions

### /api/gather/perfomers [POST]

- description: requests yandex music to find new performers and add them to database
- parameters: nickname
- result: json {'success': True}
- Example: {'nickname': 'bones'}

## Add Funtions

### /api/add/genres [POST]

- description: adds a new genre to database
- parameters: genre
- result: json {'success': True}
- Example: {'genre': 'pop'}

### /api/add/tracks [POST]

- description: adds a new track to database
- parameters: track
- result: json {'success': True}
- Example: {'track': 'swim'}

### /api/add/disks [POST]

- description: adds a new disk to database
- parameters: disk_title, disk_year
- result: json {'success': True}
- Example: {'disk': 'New tracks 2017', 'year': '2017'}

### /api/add/strings [POST]

- description: adds a new string to database
- parameters: string
- result: json {'success': True}
- Example: {"disk_fk":[2], "track_fk": [2], "genre_fk": [3], "performer_fk": [1], "duration": [188]}

## Get Funtions

### /api/get/strings

- description: gets strings from database
- result: json [{"disk_title": "Disk Title, "id": 2, "strings": [{"duration": 188, "genre_title": "Genre Title", "number": 1, "performer_name": "Performer Name", "track_title": "Track Title"}], "year": 2018}]

### /api/get/disks

- description: gets disks from database
- result: json [{"disk_id": 1, "disk_title": "Disk Title", "year": 2000}]

### /api/get/performers

- description: gets performers from database
- result: json [{"performer_id": 1, "performer_name": "Performer Name"}]

### /api/get/tracks

- description: gets tracks from database
- result: json [{"track_id": 1, "track_title": "Track Title"}]

### /api/get/tracks

- description: gets tracks from database
- result: json [{"track_id": 1, "track_title": "Track Title"}]

## Edit Funtions

### /api/edit/strings

- description: updates values in database
- parameters: old_id, old_string_number, old_disk_fk, old_track_fk, old_genre_fk, old_performer_fk, old_duration, new_id, new_string_number, new_disk_fk, new_track_fk, new_genre_fk, new_performer_fk, new_duration
- result: json {'success': True}
- example: {"old_disk_fk": 1, "old_genre_fk": 3, "new_disk_fk": 2, "new_genre_fk": 1}

### /api/edit/disks

- description: updates values in database
- parameters: old_disk_id, old_disk_title, old_year, new_disk_id, new_disk_title, new_disk_id
- result: json {'success': True}
- example: {"old_disk_id": 1, "new_disk_id": 2}

### /api/edit/tracks

- description: updates values in database
- parameters: old_track_id, old_track_title, new_track_id, new_track_title
- result: json {'success': True}
- example: {"old_track_title": "Hello", "new_track_title": "Bye"}

### /api/edit/performers

- description: updates values in database
- parameters: old_performer_id, old_performer_name, new_performer_id, new_peformer_name
- result: json {'success': True}
- example: {"old_performer_name": "Hello", "new_performer_name": "Bye"}

### /api/edit/genres

- description: updates values in database
- parameters: old_genre_id, old_genre_title, new_genre_id, new_genre_title
- result: json {'success': True}
- example: {"old_genre_title": "Hello", "new_genre_title": "Bye"}

## Delete Functions

### /api/delete/strings

- description: deletes values in database
- parameters: id, string_number, disk_fk, track_fk, genre_fk, performer_fk, duration
- result: json {'success': True}
- example: {"disk_fk": 1, "genre_fk": 3, "string_number": 10}

### /api/delete/disks

- description: deletes values in database
- parameters: disk_id, disk_title, year
- result: json {'success': True}
- example: {"year": 1907}

### /api/delete/tracks

- description: deletes values in database
- parameters: track_id, track_title
- result: json {'success': True}
- example: {"track_id": 1}

### /api/delete/performers

- description: deletes values in database
- parameters: performer_id, performer_name
- result: json {'success': True}
- example: {"performer_name": "Performer Name"}

### /api/delete/genres

- description: deletes values in database
- parameters: genre_id, genre_title
- result: json {'success': True}
- example: {"genre_title": "Genre Title"}