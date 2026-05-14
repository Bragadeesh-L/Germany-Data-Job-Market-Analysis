import requests
import pandas as pd
import time
import os

#API endpoint
url = "https://rest.arbeitsagentur.de/jobboerse/jobsuche-service/pc/v4/jobs"

#CSV output location
output_path = "data/raw/data_jobs.csv"

#Request headers
headers = {
    "X-API-Key": "jobboerse-jobsuche",
    "User-Agent": "Mozilla/5.0"
}

#Roles to search
roles = [
    "data scientist",
    "data analyst",
    "data engineer",
    "ml engineer",
    "business analyst"
]

def fetch_jobs():

    all_jobs = []

    request_count = 0
    failed_requests = 0

    #Used to avoid duplicate job records
    seen_jobs = set()

    for role in roles:

        print(f"\nFetching jobs for role: {role}")

        page = 1

        #Pagination loop
        while page <= 50:

            params = {
                "was": role,
                "wo": "Deutschland",
                "size": 25,
                "page": page
            }

            #API request
            response = requests.get(
                url,
                headers=headers,
                params=params,
                timeout=10
            )

            request_count += 1

            #Handle failed requests
            if response.status_code != 200:

                failed_requests += 1

                print(f"Failed request at Page: {page} for Role: {role}")

                break

            #Convert API response to JSON
            try:
                data = response.json()

            except ValueError:

                failed_requests += 1

                print(f"Invalid JSON at Page: {page} for Role: {role}")

                break

            jobs = data.get("stellenangebote", [])

            #Stop if no more jobs are available
            if not jobs:
                break

            for job in jobs:

                job_id = job.get("refnr")

                #Skip duplicate jobs
                if job_id in seen_jobs:
                    continue

                seen_jobs.add(job_id)

                #Store required fields
                all_jobs.append({
                    "role": role,
                    "title": job.get("titel"),
                    "company": job.get("arbeitgeber"),
                    "city": job.get("arbeitsort", {}).get("ort")
                })

            print(f"Completed page {page} for {role}")

            page += 1

            #Delay to avoid excessive API requests
            time.sleep(1)

    #Load extracted records into a dataframe
    df = pd.DataFrame(all_jobs)

    #Create a folder if it does not exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    #Export raw dataset
    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print("\nExtraction completed")
    print(f"Total records: {len(df)}")
    print(f"Total API calls: {request_count}")
    print(f"Failed requests: {failed_requests}")


if __name__ == "__main__":
    fetch_jobs()
