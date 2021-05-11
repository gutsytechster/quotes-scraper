from itemadapter import ItemAdapter  # pragma: no cover


class QuotePipeline:  # pragma: no cover
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("quote"):
            # clean quote text by removing start and end quotes
            adapter["quote"] = adapter.get("quote").strip("“”")
        return item
