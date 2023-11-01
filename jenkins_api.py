import csv
def List_job(jenkins_url,jenkins_user,jenkins_pass):
    import jenkins
    jen_server = jenkins.Jenkins(jenkins_url, username=jenkins_user, password=jenkins_pass)
    user = jen_server.get_whoami()
    jobs = jen_server.get_jobs()

    Job_stats=[]
    for i in jobs:
        Job_name =i['name']
        Job_url = i['url'] 
        job_status= i['color']
        Job_stats.append([Job_name,Job_url,job_status])
    return(Job_stats)

# List_job('http://45.33.11.12:8080','utrains','devops')

# with open ("example.txt", 'a') as f:
#     content ="adding data into file\n"
#     f.write(content)

# with open ("example.txt" , 'r') as file:
#     content= file.read()
#     print(content)
data=List_job('http://45.33.11.12:8080','utrains','devops')
with open("Jenkins_object.csv", 'w') as j:
    write_row = csv.writer(j)
    write_row.writerow(['JOB_NAME', 'JOB_URL', 'JOB_STATUS'])