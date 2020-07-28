from typing import Text, Type, Callable
from dataclasses import dataclass, field
from gitlab import Gitlab, config, exceptions

@dataclass
class GitLabBase:
  url: Type[Text] = field(default="https://gitlab.com")
  token: Type[Text] = field(repr=False, default_factory=Text)

  @property
  def client(self) -> Gitlab:
    try:
      instance = Gitlab(
        self.url,
        private_token=self.token
      )
      instance.auth()
    except exceptions.GitlabAuthenticationError as error:
      print(f"GitLab authenticantion error - {error}")
      exit()
    else:
      return instance
