from rdflib import Graph, SH
from prettytable import PrettyTable


def get_pretty_table_output(is_conform: bool, v_graph: Graph) -> str:
    result_string = ""

    t1 = PrettyTable()
    t1.field_names = ["Conforms"]
    t1.align = "c"
    t1.add_row([is_conform])
    result_string += str(t1)
    result_string += "\n\n"

    def col_widther(s, w):
        """Split strings to a given width for table"""
        s2 = []
        i = 0
        while i < len(s):
            s2.append(s[i : i + w])
            i += w
        return "\n".join(s2)

    if not is_conform:
        t2 = PrettyTable()
        t2.field_names = [
            "No.",
            "Severity",
            "Focus Node",
            "Result Path",
            "Message",
            "Component",
            "Shape",
            "Value",
        ]
        t2.align = "l"

        for i, o in enumerate(v_graph.objects(None, SH.result)):
            r = {}
            for o2 in v_graph.predicate_objects(o):
                r[o2[0]] = str(
                    col_widther(o2[1].replace(f"{SH}", ""), 25)
                )  # max col width 30 chars
            t2.add_row(
                [
                    i + 1,
                    r[SH.resultSeverity],
                    r[SH.focusNode],
                    r[SH.resultPath] if r.get(SH.resultPath) is not None else "-",
                    r[SH.resultMessage],
                    r[SH.sourceConstraintComponent],
                    r[SH.sourceShape],
                    r[SH.value] if r.get(SH.value) is not None else "-",
                ]
            )
            t2.add_row(["", "", "", "", "", "", "", ""])
        result_string += str(t2)

    return result_string
