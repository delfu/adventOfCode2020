def input_reader(inputFilePath, func, num_lines_per_case=-1):
    results = []
    with open(inputFilePath) as inputFile:
        case_builder = []
        for line in inputFile:
            if len(case_builder) == num_lines_per_case:
                results.append(func(case_builder))
                case_builder = []
            line = line.strip()
            case_builder.append(line)
        if len(case_builder) == num_lines_per_case or num_lines_per_case == -1:
            results.append(func(case_builder))
    return results
