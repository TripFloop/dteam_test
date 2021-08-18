def generate_shorten_link(endpoint=None):
    if not endpoint:
        endpoint = ''.join([
            random.choice(string.ascii_letters) for _ in range(
                settings.SHORTEN_LINK_ENDPOINT_LENGTH
            )
        ])
    return build_full_shorten_link(endpoint)
