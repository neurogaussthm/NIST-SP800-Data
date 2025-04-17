import requests
import time

ollama_api_url = "http://localhost:11434/api/generate"

#with open("./models.txt", "r") as f:
#    model_names = [name.strip() for name in f.readlines()]
#model_names = [name for name in model_names if name != '']

llmset = {1: ["granite3.1-dense:2b", "granite3.1-NIST2", "granite3.1-NIST6"], 2: ["granite3.2:2b", "granite3.2-NIST2", "granite3.2-NIST6"]}

def query_ollama(prompt, llm_model):
    response = requests.post(ollama_api_url, json={"model": llm_model, "prompt": prompt, "stream": False})
    response.raise_for_status()
    return response.json()["response"]

if __name__ == "__main__":
    with open("question-set-0-expanded.txt", 'r') as f:
        qs = f.readlines()
    for i, set in llmset.items():
        gdict = {}
        gtimes = {}
        outfile = f"../comparison/g{i}-type-q0-responses.txt"
        numresponse = 0
        for llm in set:
            name = '' if ':' in llm else llm.split('.' + str(i))[-1]
            llmout = f"../comparison/g{i}{name}-q0-responses.txt"
            start_total = time.perf_counter()
            qnum = 0
            for q in qs:
                if q[0] != '#':
                    start_time = time.perf_counter()
                    answer = query_ollama(q, llm)
                    total_time = time.perf_counter() - start_time
                    output = f"\nAnswer from {llm} ({total_time}): \n\"\"\"{answer}\"\"\"\n"
                    if q not in gdict:
                        gdict[q] = [output]
                    else:
                        gdict[q].append(output)
                    print(f"{llm}, question: {qnum}")
                    qnum += 1
                    time.sleep(0.05)
            total_total = time.perf_counter() - start_total
            gtimes[llm] = total_total
            string = f"{llm}: total time = {total_total}\n"
            for k, v in gdict.items():
                string += f"\n{k}\n\n{v[numresponse]}\n"
            with open(llmout, "w") as f:
                f.write(string)
            numresponse += 1
        string = ""
        for k, v in gtimes.items():
            string += f"{k}: total time = {v}\n"
        with open(outfile, 'w') as f:
            f.write(string + '\n')
        for k, v in gdict.items():
            with open(outfile, 'a') as f:
                f.write(f"\n\n{k}\n\n{''.join(v)}")
