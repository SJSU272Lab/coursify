import scrapy
import re
import time

class DepartmentCourses(scrapy.Spider):
    name = "department_courses"

    courses = list()
    prereq_list = list()

    def start_requests(self):
        urls = [
            'http://info.sjsu.edu/web-dbgen/catalog/departments/CMPE-courses.html',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_department_page)

    def parse_department_page(self, response):
        #page = response.url.split("/")[-2]
        self.courses = response.css('div.info_wrapper td a::text').re(r'(.*):')
        course_url = response.css('div.info_wrapper td a::attr(href)').extract()
        for url in course_url:
            url = "http://info.sjsu.edu/" + str(url)
            self.log("next url is " + url)
            yield scrapy.Request(url=url, callback=self.parse_course_page)
        ##yield self.prereq_list 
        self.log("Prereq courses : " + str(self.prereq_list))

    def parse_course_page(self, response):
        course_name  = str(response.css('div.info_wrapper h3::text').extract()[0])
        course_description =  str(response.css('div.info_wrapper p::text').extract()[1])
        self.log("Finding prereqiste for " + course_name)
        temp = {}
        for course in self.courses:
            pre_req_search = re.search("[Pp]rerequisite[s]?:[ ,\"\-:(\w)*]+", course_description, re.IGNORECASE)
            if pre_req_search:
               self.log("pre req search result " + pre_req_search.group(0) ) 
               if re.search(course, pre_req_search.group(0), re.IGNORECASE):
                  if course_name in temp:
                    temp[course_name]["prereq"].append(course)
                  else:
                    temp[course_name] ={}
                    temp[course_name]["coreq"] = []
                    temp[course_name]["prereq"] = [course]
            co_req_search = re.search("[cC]orequisite[s]?:[ :,\"\-(\w)]+", course_description, re.IGNORECASE)
            if co_req_search:
               self.log("co req search result " + pre_req_search.group(0) )
               if re.search(course, co_req_search.group(0), re.IGNORECASE):
                  if course_name in temp:
                    temp[course_name]["coreq"].append(course)
                  else:
                    temp[course_name] ={}
                    temp[course_name]["prereq"]=[]
                    temp[course_name]["coreq"] = [course]
        if not (len(temp) == 0):
           yield temp

                    
