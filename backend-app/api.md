# DOCFILE ABOUT API

## /api/gather/perfomers [POST]

- description: requests yandex music to find new performers and add them to database
- parameters: nickname
- result: json {'success': True}
- Example: {'nickname': 'bones'}

## /api/add/genres [POST]

- description: adds a new genre to database
- parameters: genre
- result: json {'success': True}
- Example: {'genre': 'pop'}

## /api/add/tracks [POST]

- description: adds a new track to database
- parameters: track
- result: json {'success': True}
- Example: {'track': 'swim'}

## /api/add/disks [POST]

- description: adds a new disk to database
- parameters: disk_title, disk_year
- result: json {'success': True}
- Example: {'disk': 'New tracks 2017'}

## /api/add/strings [POST]

- description: adds a new string to database
- parameters: string
- result: json {'success': True}
- Example: {'disk': 'New tracks 2017'}