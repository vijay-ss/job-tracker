import requests
import json
from send_email import send_email

URL = "https://remoteok.io/api"
keys = ['date', 'company', 'position', 'tags', 'location', 'url']

wanted_tags = ['python', 'data', 'product manager', 'engineer', 'manager', 'scientist']

def get_jobs():
    resp = requests.get(URL)
    job_results = resp.json()
    
    jobs = []
    for job_res in job_results:
        # take only the specified keys
        job = {k: v for k, v in job_res.items() if k in keys}
    
        if job:
            tags = job.get('tags')
            tags = {tag.lower() for tag in tags}
            if tags.intersection(wanted_tags):
                jobs.append(job)
    #print(jobs)
    return jobs



if __name__ == '__main__':
    job_alert = get_jobs()

    if job_alert:
        message = "Subject: Interesting Jobs! From my web scraper"
        message += "Found some cool jobs!"

        for job in job_alert:
            message += f"{json.dumps(job)}\n\n"

        send_email(message)

