from urllib import robotparser
robot_parser=robotparser.RobotFileParser()#robotparser module allows you to check rules from robots.txt file
def prepare(robots_txt_url):
    robot_parser.set_url(robots_txt_url)#taking the url of website
    robot_parser.read()#opening the website and readu=ing the rules
def is_allowed(tangent_url,user_agent="*"):#* represents all and tangenturl is for the part of the website must checked
    return robot_parser.can_fetch(user_agent,tangent_url)
if __name__=="__main__":
    prepare("http://www.apress.com/robots.txt")
    print(is_allowed("http://www.apress.com/covers/"))
    print(is_allowed("http://www.apress.com/gp/python"))
    
