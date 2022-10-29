cdef class IncrementalGenerator:
    cdef public str name
    cdef public bytes file_content
    cdef public int progress

    cpdef bytes get_bytes(self, int n, int update_progress = *)

    cpdef bytes get_remaining_bytes(self)
