from datetime import datetime
import colorama


class Logger:
    """
    This class is used to log in different modes:
    debug
    info
    warn
    error
    """

    def debug(self, message: str, exception: Exception = None) -> None:
        """
        This function print the message in debug mode
        """
        print(f"[DEBUG] - {datetime.now().time()} - {message}")

    def info(self, message: str, exception: Exception = None) -> None:
        """
        This function print the message in info mode
        """

        print(
            f"{colorama.Back.BLUE}[INFO] - {datetime.now().time()} - {message}{colorama.Back.RESET}"
        )

    def warn(self, message: str, exception: Exception = None) -> None:
        """
        This function print the message in warn mode
        """

        print(
            f"{colorama.Back.LIGHTRED_EX}[WARN] - {datetime.now().time()} - {message}{colorama.Back.RESET}"
        )

    def error(self, message: str, exception: Exception = None) -> None:
        """
        This function print the message in error mode
        """

        print(
            f"{colorama.Back.RED}[ERROR] - {datetime.now().time()} - {message}{colorama.Back.RESET}"
        )
