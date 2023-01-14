"use strict";
module.exports = [{
    names: ["Check-Note-notation"],
    description: "Checking **Note** notations...\n",
    tags: ["notes", "markdown"],
    function: (params, onError) => {
        params.lines.forEach(function forLine(line, lineNumber) {
            if(line.match(/^\*\*Note\*\*/)){
                if(!params.lines[lineNumber-1].match(/^> \*\*Note\*\*$/)){
                    onError({
                        lineNumber: lineNumber+1,
                        detail: "\nThe below phrase '**Note**' should be preceded by '> **Note**'\n",
                        context: line
                    });
                }
            }
        });
    }
}, {
    names: ["Check-Warning-notation"],
    description: "Checking **Warning** notations...\n",
    tags: ["warning", "markdown"],
    function: (params, onError) => {
        params.lines.forEach(function forLine(line, lineNumber) {
            if(line.match(/^\*\*Warning\*\*/)){
                if(!params.lines[lineNumber-1].match(/^> \*\*Warning\*\*$/)){
                    onError({
                        lineNumber: lineNumber+1,
                        detail: "\nThe below phrase '**Warning**' should be preceded by '> **Warning**'\n",
                        context: line
                    });
                }
            }
        });
    }
}];