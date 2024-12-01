from sys import stdout


def ft_tqdm(lst: range) -> None:  # type: ignore
    """Recreated tqdm function.

    Args:
        lst (range): A range object.

    Yields:
        int: The current index.
    """
    BAR_MAX_LEN = 100
    BAR_CHAR = "█"
    for i in lst:
        progress_rate = (i + 1) / len(lst)
        progress_rate_str = f"{(progress_rate * 100):.0f}%".rjust(4)
        bar_len = int(progress_rate * BAR_MAX_LEN)
        bar_str = "|" + (BAR_CHAR * bar_len).ljust(BAR_MAX_LEN) + "|"

        stdout.write(f"\r{progress_rate_str}{bar_str} {i + 1}/{len(lst)}")
        stdout.flush()
        yield i
    stdout.write("\n")
