#!/usr/bin/env python3

from vial import Vial
from nxtools import *
from unimatrix import Unimatrix


matrix = Unimatrix()


class App(Vial):
    def handle(self, request):
        try:
            dest = int(path(0))
        except IndexError:
            dest = None
        except ValueError:
            return self.response(400)

        if not dest in matrix.destinations:
            return self.response(404)

        if request.method == "OPTIONS":
            #TODO handle preflight request
            pass
        if request.method == "POST":
            #
            pass

        if dest:
            pass


        return self.response(200, data=data)



app = App()

if __name__ == "__main__":
    app.serve()


