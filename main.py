from datetime import date


# Currying in Pytong
def log(when):
    def _what(what):
        def _why(why):
            print("{}: [{}] -> {}".format(when, what, why))
        return _why
    return _what


log(date.today())("[ERROR]")("File could not be opened")

log_now = lambda what, why:  log(date.today())(what)(why)
log_now("WARN", "Zip is open")

log_now_info = lambda why : log(date.today())("INFO")(why)
log_now_info("I've a feeling we're not in Kansas anymore")


# But How do I get JS style
# log_now("WARN")("Zip is open")
# instead of
log_now("WARN", "Zip is open")
