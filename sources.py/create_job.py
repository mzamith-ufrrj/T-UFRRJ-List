import sys
import time
import platform
import asyncio
from pprint import pprint


async def run_command(*args):
    # Create subprocess
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    # Status
    print("Started: %s, pid=%s" % (args, process.pid), flush=True)

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print(
            "Done: %s, pid=%s, result: %s"
            % (args, process.pid, stdout.decode().strip()),
            flush=True,
        )
    else:
        print(
            "Failed: %s, pid=%s, result: %s"
            % (args, process.pid, stderr.decode().strip()),
            flush=True,
        )

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result


def run_asyncio_commands(tasks, max_concurrent_tasks=0):

    all_results = []
    chunks = [tasks]
    num_chunks = len(chunks)

    if asyncio.get_event_loop().is_closed():
        asyncio.set_event_loop(asyncio.new_event_loop())

    loop = asyncio.get_event_loop()

    chunk = 1
    for tasks_in_chunk in chunks:
        print(
            "Beginning work on chunk %s/%s" % (chunk, num_chunks), flush=True
        )
        commands = asyncio.gather(*tasks_in_chunk)  # Unpack list using *
        results = loop.run_until_complete(commands)
        all_results += results
        print(
            "Completed work on chunk %s/%s" % (chunk, num_chunks), flush=True
        )
        chunk += 1

    loop.close()
    return all_results


def main():
    """Main program."""
    start = time.time()

    # Commands to be executed on Unix
    commands = [["du", "-sh", "/var/tmp"], ["hostname"]]

    tasks = []
    for command in commands:
        tasks.append(run_command(*command))



    # # List comprehension example
    # tasks = [
    #     run_command(*command, get_project_path(project))
    #     for project in accessible_projects(all_projects)
    # ]

    results = run_asyncio_commands(
        tasks, max_concurrent_tasks=20
    )  # At most 20 parallel tasks
    print("Results:")
    pprint(results)

    end = time.time()
    rounded_end = "{0:.4f}".format(round(end - start, 4))
    print("Script ran in about %s seconds" % (rounded_end), flush=True)


if __name__ == "__main__":
    main()