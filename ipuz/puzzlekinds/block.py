from ipuz.validators import validate_bool


IPUZ_BLOCK_VALIDATORS = {
    "slide": validate_bool,
    "move": validate_bool,
    "rotatable": validate_bool,
    "flippable": validate_bool,
}
