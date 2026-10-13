from checker import (
    build_url,
    is_https,
    show_response,
    check_site,
    scan_sites,
    check_headers,
    retry_check,
)

print("=== Partea 1: Funcții ajutătoare ===")
print("build_url fără /:", build_url("example.com", "login"))
print("build_url cu /:", build_url("example.com", "/login"))
print("is_https (True):", is_https("https://example.com"))
print("is_https (False):", is_https("http://example.com"))

print("\n=== Partea 2: Trimiterea unei cereri ===")
show_response("https://example.com")

print("\n=== Partea 3: Un verificator reutilizabil ===")
print("check_site (succes):", check_site("https://example.com"))
print("check_site (inexistent):", check_site("http:// acest-site-nu-exista.invalid"))

print("\n=== Partea 4: Verificarea mai multor site-uri ===")
scan_sites()

print("\n=== Partea 5: Audit de securitate ===")
print("check_headers (cu antete):", check_headers("https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff"))

print("\n=== Partea 6: Încercări repetate ===")
print("retry_check (200 OK):", retry_check("https://httpbin.org/status/200"))
print("retry_check (404 Not Found):", retry_check("https://httpbin.org/status/404"))
print("retry_check (500 Server Error):", retry_check("https://httpbin.org/status/500"))
print("retry_check (site invalid):", retry_check("http://acest-site-nu-exista.invalid"))