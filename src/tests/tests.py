import GithubProfile as gf


p = gf.get_github_profile('swingfufufu')

print(p.login + ":\t " + p.name + ":\t " + p.avatar_url+ ":\t " + p.html_url )

