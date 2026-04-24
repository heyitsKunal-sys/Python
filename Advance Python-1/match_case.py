# MATCH CASE
# SIMILAR TO SWITCH LIKE IN OTHER LANGUAGES

def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404 :
             return"not found"
        case 500:
             return"internal server errors"
        case _:
             return "unknown status"

# Usage
print(http_status(200))  # Output: OK 
print(http_status(404))  # Output: Not Found 
print(http_status(500))  # Output: Internal Server Error 
print(http_status(403))  # Output: Unknown status 
    